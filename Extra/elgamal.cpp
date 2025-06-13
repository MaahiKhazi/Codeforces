#include <iostream>
#include <math.h>
#include <cstdlib>
#include <vector>
using namespace std;

int main()
{
    int modulus, p;
    cout << "Enter the value of P (prime modulus): \n";
    cin >> p;
    modulus = p;
    int x_values[p], y_values[p], a, b, i, j;

    cout << "\nEnter the Value of 'a' in the equation: \n";
    cin >> a;
    cout << "\nEnter the Value of 'b' in the equation: \n";
    cin >> b;
    cout << "\nElliptic Curve Equation: y^2 mod " << p << " = (x^3  + " << a << "*x + " << b << ") mod " << p << "\n\n\n";

    vector<int> valid_x_points;
    vector<int> valid_y_points;

    // Calculate y values for all x values in range 0 to p-1
    for (int i = 0; i < p; i++)
    {
        x_values[i] = i;
        y_values[i] = ((i * i * i) + a * i + b) % p;
    }

    // Generate Base Points
    int count = 0;
    for (i = 0; i < p; i++)
    {
        for (j = 0; j < p; j++)
        {
            if (y_values[i] == (x_values[j] * x_values[j]) % p)
            {
                count++;
                valid_x_points.push_back(x_values[i]);
                valid_y_points.push_back(y_values[j]);
            }
        }
    }

    cout << endl
         << "Generated Points on the curve:" << endl;

    for (i = 0; i < count; i++)
    {
        cout << i + 1 << "\t( " << valid_x_points[i] << " , " << valid_y_points[i] << " )" << endl;
    }
    cout << "Base Point: (" << valid_x_points[0] << "," << valid_y_points[0] << ")"
         << "\n";
    int private_key, d, message;
    cout << "Enter the private key 'd' for Sender (d < n)\n";
    cin >> d;
    int Qx = d * valid_x_points[0];
    int Qy = d * valid_y_points[0];
    // Q is the public key of sender

    // Encryption
    int random_number_k;
    cout << "Enter the random number 'k' (k < n)\n";
    cin >> random_number_k;

    cout << "Enter the message to be sent:\n";
    cin >> message;
    cout << "The message to be sent is:\n"
         << message << "\n";

    int c1x = random_number_k * valid_x_points[0];
    int c1y = random_number_k * valid_y_points[0];
    cout << "Value of C1: (" << c1x << "," << c1y << ")"
         << "\n";

    int c2x = random_number_k * Qx + message;
    int c2y = random_number_k * Qy + message;
    cout << "Value of C2: (" << c2x << "," << c2y << ")"
         << "\n";

    // Decryption
    cout << "\nThe received message is:\n";
    int decrypted_message_x = c2x - d * c1x;
    int decrypted_message_y = c2y - d * c1y;
    cout << decrypted_message_x << endl;
    return 0;
}
