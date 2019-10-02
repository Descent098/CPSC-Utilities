/**
The simplest solution for this is to use recursion. See the code below for the solution.

NOTE: Code primarily transpiled from source below.
SEE: https://www.youtube.com/watch?v=8lhxIOAfDss
*/
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Printf("How many discs are on the tower?: ")
	var discs int
	_, err := fmt.Scanf("%d", &discs)
	if err != nil {
		os.Exit(0)
	}
	hanoi(discs, "A", "B", "C")
}

func move(moveFrom string, moveTo string) {
	fmt.Printf("Move disc from %s to %s!\n", moveFrom, moveTo)
}

func hanoi(numOfDiscs int, moveFrom string, helper string, moveTo string) {
	if numOfDiscs == 0 { // Base Case

	} else { // solve remaining puzzle
		hanoi(numOfDiscs-1, moveFrom, moveTo, helper)
		move(moveFrom, moveTo)
		hanoi(numOfDiscs-1, helper, moveFrom, moveTo)
	}
}
