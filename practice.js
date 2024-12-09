// // function sum_array(array) {
// //     let new_array = []
// //     let count = 0
// //     for (i = 0; i < array.length; i ++) {
// //         if (array[i][0].startsWith("a")) {
// //             new_array.push(array[i])
// //             count += 1
// //         }
// //     }
// //     return new_array
// // }

// // // array = ["apple", "banana", "apricot"]
// // // console.log(sum_array(array))

// // function true_number(array, number) {
// //     for (i = 0; i < array.length; i ++) {
// //         if (number == array[i]) {
// //             return i
// //         }
// // }
// // //     return -1
// // // }
// // console.log(true_number([1, 7, 4, 9, 8], 7))



// //     let blue = "blue"
// //     let green = "green"
// //     let yellow = "yellow"
// //     let array = []

// //     for (i = 0; i < 100; i ++) {
// //         if (i <= 50 ) {
// //             array.push(blue)
// //         }
// //         if (i <=75) {
// //             array.push(green)
// //         }
// //         if (i <= 100) {
// //             array.push(yellow)
// //         }
// //     }

// //   var item = array[Math.floor(Math.random()*array.length)];
// //   console.log(item)


// // function sum_array(array, number) {
// //     let new_array = []
// //     for (i = 0; i < array.length; i ++) {
// //         if (array[i] == number) {
// //             return i
// //         } else {
// //             new_array.push(array[i])
// //         }
// //     }
// //     return new_array
// // }

// // console.log(sum_array([1, 5, 5, 4, 3, 4], 7))


// // function starts_with(array) {
// //     let new_array = []
// //     for (i = 0; i < array.length; i ++) {
// //         if (array[i][0].startsWith("a")) {
// //             new_array.push(array[i])
// //         }
// //     }
// //     return new_array
// // }
 
// // console.log(starts_with(["apple", "bottom", "jeans", "apricot"]))

// let blue = "blue"
// let green = "green"
// let yellow = "yellow"
// let array = []

// for (i = 0; i < 100; i ++) {
//     if (i <= 30) {
//         array.push(blue)
//     } else {
//         if (i <= 60) {
//             array.push(green)
//         } else {
//             if ( i <= 100) {
//                 array.push(yellow)
//             }
//         }
//     }
    
// }

// var item = array[Math.floor(Math.random()*array.length)];
// console.log(item)


// Write a while loop to print the numbers 1 through 10.

// function print_one(number) {
//     while (number <= 10) {
//         console.log(number)
//         number += 1
//     }
// }

// console.log(print_one(1))

// Write a while loop that prints the word "hello" 5 times.

// count = 0

// while (count < 5) {
//     console.log("hello")
//     count += 1
// }

// count = 2

// while (count <= 40) {
//     console.log(count)
//     count += 2
// }


// Make a hash to store a person's first name, last name, and email address. Then print each attribute on separate lines.

// var person = {firstName: "Chazz",lastName: "Gagliano", eMail: "cg@gmail.com"}

// console.log(person.firstName)
// console.log(person.lastName)
// console.log(person.eMail)

// Make an array of hashes to store the first name and last name for 3 different people. Then print out the first person's info.

// var person = [
//     {firstName: "tim", lastName: "little"},
//     {firstName: "mike", lastName: "big"},
//     {firstName: "fred", lastName: "medium"}
// ]

// console.log(person[0])

// # Write a function that takes in a number and returns the number times two. Then run the function and print the result.

// function number_2(number) {
//     return number * 2
// }

// console.log(number_2(2))

// # 1. Write a function that takes in a number and returns the number times two. Then run the function and print the result.


// # 8. Write a function that takes in a string and returns the string repeated 5 times. Then run the function and print the result.

// function string_five(string) {
//    return string + " " + string + " " + string + " " + string + " " + string
// }

// console.log(string_five("hello"))

// Write a function that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the function and print the result.

// function sum(number1, number2, number3) {
//     return (number1 + number2 + number3) / 3
// }

// console.log(sum(3, 3, 3))

// Write a function that takes in a number and returns the number times 10 plus 30. Then run the function and print the result.

// function times10plus30(number) {
//     return (number * 10) + 30
// }

// console.log(times10plus30(4))

// let blue = "blue"
// let green = "green"
// let yellow = "yellow"
// array = []
// i = 0

// while (i <= 100) {
//     if (i <= 30) {
//         array.push(blue)
//         i += 1
//     }
//     else if (i <= 60) {
//         array.push(green)
//         i += 1
//     } else if (i <= 100) {
//         array.push(yellow)
//         i += 1
//     }
// }

// var item = array[Math.floor(Math.random()*array.length)];
// console.log(item)

// function starts_with(array) {
//         let new_array = []
//         let i = 0

//         while (i < array.length) {
//             if (array[i].name[0].startsWith("b")) {
//                 new_array.push(array[i])
//             }
//             i ++
//         }
//         return new_array
// }

// console.log(starts_with([{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}]))


// 1. Convert an array of arrays into a hash.

// var pairs = [[1, 3], [8, 9], [2, 16]];


// var pairsObject = {}
// let i = 0

// while (i < pairs.length) {
//     var key = pairs[i][0]
//     var value = pairs[i][1]
//     pairsObject[key] = value
//     i += 1
// }

// console.log(pairsObject)


// Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.

// var word = "bookkeeper";
// var object = {};
// var i = 0;
// while (i < word.length) {
    //   var letter = word[i];
    //   if (object[letter] === undefined) {
        //     object[letter] = 0;
        //   }
        //   object[letter] += 1;
        //   i += 1;
        // }
        // console.log(object);

    // Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
        
        // var items = [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}]
        // let i = 0
        // let pair = {}
        
        // while (i < items.length) {
        //     pair[items[i].id] = items[i]
        //     i ++
        // }
        
        // console.log(pair)

        // Use a nested loop to convert an array of number pairs into a single flattened array.

        // function single_array(array) {
        //     let i = 0 
        //     let new_array = []
        //     while (i < array.length) {
        //         let i2 = 0
        //         while (i2 < array[i].length) {
        //             new_array.push(array[i][i2])
        //             i2 ++
        //         }
        //         i ++ 
        //     }
        //     return new_array
        // }

        // console.log(single_array([[1, 3], [8, 9], [2, 16]]))

//         se a nested loop with two arrays of strings to create a new array of strings with each string combined.
// //     For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].


// function single_array (letters1, letters2) {
//     let i = 0
//     let combinedLetters = []
//     while (i < letters1.length) {
//         let i2 = 0
//         while (i2 < letters2.length) {
//             combinedLetters.push(letters1[i] + letters2[i2])
//             i2 ++
//         }
//         i ++
//     }
//     return combinedLetters
// }

// console.log(single_array(["a", "b", "c"], ["d", "e", "f", "g"]))


// Use a nested loop with two arrays of strings to create a new array of strings with each string combined.

function combined(array) {
    new_array = []
    for (i = 0; i < array.length; i ++) {
        for (i2 = 0; i2 < array.length; i2 ++) {
            if (i !== i2) {
                new_array.push(array[i] + array[i2])
            }
        }
    }
    return new_array
}

console.log(combined(["a", "b", "c", "d"]))