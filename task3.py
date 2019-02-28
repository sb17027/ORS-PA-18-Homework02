"""
===================   TASK 3   ====================
* Name: Cube Volume
*
* Write a function `cube_volume` that will return
* volume of a cube for a given side length.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def cube_volume(side_in_cm):
    dozvoljeni_karakteri=['0','1','2','3','4','5','6','7','8','9','.']
    for x in side_in_cm:
        if x not in dozvoljeni_karakteri:
            print("-1")
        broj_tacaka = 0

        for x in side_in_cm:
            if x == '.':
                broj_tacaka=broj_tacaka+1
            if broj_tacaka > 1:
                print("-1")
        broj_minusa=0

        for x in side_in_cm:
            if x =='-':
                broj_minusa=broj_minusa
            if broj_minusa > 1:
                print("-1")

    print(side_in_cm**3)


def main():

    side_in_cm = 5.0
    volume_of_cube = side_in_cm**3
    print("Volume of a cube is: ", volume_of_cube)

main()
