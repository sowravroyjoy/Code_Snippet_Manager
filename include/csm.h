#ifndef CSM_H
#define CSM_H

#include <iostream>
#include "sqlite3.h"
#include <string>
#include <vector>
using std::string;
using std::cout;
using std::cin;
using std::endl;


// given the name and main code as the description to add those in the sql database
void add(string name, string desc);

// given the unique id, name and main code as the description to update those in the sql database
void update(int id, string name, string desc);

// given the unique id to delete those from the sql database
void del(int id);

// show the saved code snippets
void show(sqlite3 &db);

#endif
