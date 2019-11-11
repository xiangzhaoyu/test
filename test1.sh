#!/bin/bash

test(){
    echo "this is first std"
    exit 1
}
echo "hello world"

fun2(){
    echo "this is second std"
}

test
fun2