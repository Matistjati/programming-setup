#pragma once

#include <bits/stdc++.h>
using namespace std;

// Slow versions so i can debug in msvc
typedef int set_type;

template<typename T>
class indexed_multiset : public multiset<T>
{
public:
	auto find_by_order(int idx)
	{
		return next(this->begin(), idx);
	}

	int order_of_key(T idx)
	{
		auto it = this->lower_bound(idx);
		return distance(this->begin(), it);
	}
};

template<typename T>
class indexed_set : public set<T>
{
public:
	auto find_by_order(int idx)
	{
		return next(this->begin(), idx);
	}
	
	int order_of_key(T idx)
	{
		int ret = 0;
		for (auto item : *this)
		{
			ret += item < idx;
		}
		return ret;
	}
};

template<typename T, typename U>
class indexed_map : public map<U, T>
{
public:
	auto find_by_order(int idx)
	{
		return next(this->begin(), idx);
	}
	
	int order_of_key(T idx)
	{
		int ret = 0;
		for (auto item : *this)
		{
			ret += item.first < idx;
		}
		return ret;
	}
};

template<typename T, typename U>
class fast_map : public unordered_map<T, U>
{

};

template<typename T>
class fast_set : public unordered_set<T>
{

};

template<typename T, typename H>
class fast_set_h : public unordered_set<T, H>
{

};

