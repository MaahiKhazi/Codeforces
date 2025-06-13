#include <iostream>
#include <openssl/ec.h>
#include <openssl/evp.h>
#include <openssl/pem.h>
#include <openssl/rand.h>

// Function to generate an EC key pair
EC_KEY *generate_ec_key()
{
    EC_KEY *key = EC_KEY_new_by_curve_name(NID_X9_62_prime256v1);
    if (!key)
    {
        std::cerr << "Error creating EC key pair" << std::endl;
        return nullptr;
    }
    if (!EC_KEY_generate_key(key))
    {
        std::cerr << "Error generating EC key pair" << std::endl;
        EC_KEY_free(key);
        return nullptr;
    }
    return key;
}

// Function to perform ECDH key exchange
unsigned char *perform_ecdh_key_exchange(EC_KEY *private_key, EC_KEY *public_key, size_t *shared_key_len)
{
    int shared_key_len_int;
    unsigned char *shared_key = nullptr;

    shared_key_len_int = ECDH_compute_key(nullptr, 0, EC_KEY_get0_public_key(public_key), private_key, nullptr);
    if (shared_key_len_int <= 0)
    {
        std::cerr << "Error computing ECDH shared key" << std::endl;
        return nullptr;
    }

    *shared_key_len = (size_t)shared_key_len_int;
    shared_key = (unsigned char *)malloc(*shared_key_len);
    if (!shared_key)
    {
        std::cerr << "Memory allocation error" << std::endl;
        return nullptr;
    }

    if (ECDH_compute_key(shared_key, *shared_key_len, EC_KEY_get0_public_key(public_key), private_key, nullptr) != shared_key_len_int)
    {
        std::cerr << "Error computing ECDH shared key" << std::endl;
        free(shared_key);
        return nullptr;
    }

    return shared_key;
}

int main()
{
    EC_KEY *alice_key = generate_ec_key();
    if (!alice_key)
        return 1;

    EC_KEY *bob_key = generate_ec_key();
    if (!bob_key)
    {
        EC_KEY_free(alice_key);
        return 1;
    }

    // Perform key exchange from Alice's perspective
    size_t shared_key_len_alice;
    unsigned char *shared_key_alice = perform_ecdh_key_exchange(alice_key, EC_KEY_get0_public_key(bob_key), &shared_key_len_alice);
    if (!shared_key_alice)
    {
        EC_KEY_free(alice_key);
        EC_KEY_free(bob_key);
        return 1;
    }

    // Perform key exchange from Bob's perspective
    size_t shared_key_len_bob;
    unsigned char *shared_key_bob = perform_ecdh_key_exchange(bob_key, EC_KEY_get0_public_key(alice_key), &shared_key_len_bob);
    if (!shared_key_bob)
    {
        free(shared_key_alice);
        EC_KEY_free(alice_key);
        EC_KEY_free(bob_key);
        return 1;
    }

    // Compare shared keys
    if (shared_key_len_alice != shared_key_len_bob || memcmp(shared_key_alice, shared_key_bob, shared_key_len_alice) != 0)
    {
        std::cerr << "Error: Shared keys do not match" << std::endl;
        free(shared_key_alice);
        free(shared_key_bob);
        EC_KEY_free(alice_key);
        EC_KEY_free(bob_key);
        return 1;
    }

    std::cout << "Keys established successfully!" << std::endl;
    std::cout << "Shared Key: ";
    for (size_t i = 0; i < shared_key_len_alice; ++i)
    {
        printf("%02x", shared_key_alice[i]);
    }
    std::cout << std::endl;

    free(shared_key_alice);
    free(shared_key_bob);
    EC_KEY_free(alice_key);
    EC_KEY_free(bob_key);

    return 0;
}