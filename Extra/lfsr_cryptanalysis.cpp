#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> polynomial_division(vector<int> &f, vector<int> &g, vector<int> &rem)
{
    vector<int> q(f.size() - g.size() + 1, 0);
    while (f.size() >= g.size())
    {
        int factor = f.back() / g.back();
        int deg_diff = f.size() - g.size();
        for (int i = 0; i < g.size(); i++)
        {
            f[i + deg_diff] -= factor * g[i];
        }
        q[deg_diff] = factor;
        f.pop_back();
    }
    rem = f;
    return q;
}

vector<int> Extended_euclidean_poly(vector<int> &f, vector<int> &g, vector<int> &u, vector<int> &v)
{
    if (g.size() == 0)
    {
        u = {1};
        v = {};
        return f;
    }
    vector<int> rem;
    vector<int> u1, v1;
    vector<int> q = polynomial_division(f, g, rem);
    vector<int> gcd = Extended_euclidean_poly(g, rem, u1, v1);
    u = v1;
    vector<int> temp = polynomial_division(u1, q, v);

    for (int i = 0; i < temp.size(); i++)
    {
        v[i] = u[i] - temp[i];
    }
    return gcd;
}

int main()
{
    vector<int> A, B;
    int n, m;
    cout << "Enter the no. of terms in A: ";
    cin >> n;
    cout << "Enter the coeff of A: ";
    for (int i = 0; i < n; ++i)
    {
        int element;
        cin >> element;
        A.push_back(element);
    }
    cout << "Enter the no. of terms in B: ";
    cin >> m;
    cout << "Enter the coeff of B: ";
    for (int i = 0; i < m; ++i)
    {
        int element;
        cin >> element;
        B.push_back(element);
    }
    vector<int> u, v;
    vector<int> gcd;
    gcd = Extended_euclidean_poly(A, B, u, v);
    for (int i = 0; i < gcd.size(); i++)
    {
        cout << gcd[i];
    }
    cout << "Multiplicative Inverse of f is : ";
    for (int i = 0; i < u.size(); i++)
    {
        cout << u[i];
    }
    cout << "Multiplicative Inverse of g is : ";
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i];
    }
}


