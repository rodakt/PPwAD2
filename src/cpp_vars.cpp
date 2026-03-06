/* src/cpp_vars.cpp */
#include <iostream>

int main(){
    int a = 1, b; // deklaracja zmiennych a, b
    b = a; // b ma te sama wartosc co a

    std::cout  << "a: " << a << ", b: " << b << std::endl;
    std::cout << "adres a: " << &a << ", adres b: " << &b << std::endl;

    a = 123; // wartosc a jest zmieniana, obszar w pamieci nie

    std::cout  << "\na: " << a << ", b: " << b << std::endl;
    std::cout << "adres a: " << &a << ", adres b: " << &b << std::endl;

    return 0;
}