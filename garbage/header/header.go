package main

import (
   "fmt"
   "math/rand"
   "time"
)

// generates a random petal
func petal() string {
   // a seed for rand
   var random = rand.New(rand.NewSource(time.Now().UnixNano()))
   // return the petal
   return random
   //return "▪"
}

// prints my beautiful header
func main() {
   var petal string = petal()
   fmt.Print(petal)
   fmt.Print("\n")
}