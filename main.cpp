#include <iostream>
#include <fstream>
#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

bool cmp(pair<string, int> &a,
         pair<string, int> &b)
{
  return a.second < b.second;
}

void to_lowercase(string &s)
{
  for_each(s.begin(), s.end(), [](char &c)
           { c = tolower(c); });
}

void print_map(unordered_map<string, int> map)
{
  vector<pair<string, int>> dict_list;
  for (auto &it : map)
  {
    dict_list.push_back(it);
  }
  sort(dict_list.begin(), dict_list.end(), cmp);
  for (auto &it : dict_list)
  {
    if (it.first == "")
    {
      continue;
    }
    cout << it.first << "\t:\t" << it.second << endl;
  }
}

void string_to_word_map(unordered_map<string, int> &map, string s)
{
  to_lowercase(s);
  string word = "";
  for (auto x : s)
  {
    if ((x >= 'a' && x <= 'z') || x == '\'')
    {
      word = word + x;
    }
    else
    {
      map[word]++;
      word = "";
    }
  }
}

int main(int argc, char const *argv[])
{

  unordered_map<string, int> Mymap;
  fstream fs("content.txt", ios::in);
  string line;
  while (fs)
  {
    getline(fs, line);
    string_to_word_map(Mymap, line);
  }
  fs.close();
  print_map(Mymap);
  return 0;
}
