#include <iostream>
using namespace std;

class Student
{

private:
    string home_address;
    int remaining_dues;

public:
    int roll_number;
    string name;

    void get_data()
    {
        cout << "Enter Home Address = ";
        cin >> home_address;
        cout << "Enter Remaining dues";
        cin >> remaining_dues;
        cout << "Roll Number = ";
        cin >> roll_number;
        cout << "Name = ";
        cin >> name;
    }

    void info()
    {
        cout << "Home Address is = " << home_address << endl;
        cout << "Remaining Dues are = " << remaining_dues << endl;
        cout << "His roll Number is = " << roll_number << endl;
        cout << "The name of this student is = " << name << endl;
    }
};

int main()
{
    Student std;
    std.get_data();
    std.info();
    return 0;
}