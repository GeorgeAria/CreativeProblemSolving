//How arrays are initialized
let shopping = ['bread', 'milk',  'cheese', 'hummus', 'noodles'];
shopping;

//How to access a value from an array
shopping[0];
shopping[0] = 'tahini';
shopping;
shopping.length;

//.length allows you to loop through the contents of an array
let sequence = [1, 1, 2, 3, 5, 8, 13];
for(let i = 0; i < sequence.length; i++)
{
    console.log(sequence[i]);
}

//split() allows you to split the contents of a String value based on a certain character and inserts those contents into an array
let myData = 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle';
let myArray = myData.split(',');
myArray;
myArray.length;
myArray[0]; // the first item in the array
myArray[1]; // the second item in the array
myArray[myArray.length-1]; // the last item in the array

//join() turns array contents to single String value with a character you choose in between values
let myNewString = myArray.join('/');
myNewString;

//toString() turns array contents to single String value with a comma between entries
let dogNames = ['Rocket','Flash','Bella','Slugger'];
dogNames.toString(); //Rocket,Flash,Bella,Slugger

//Add items to the end of an array with push()
myArray.push('Cardiff');
myArray;
myArray.push('Bradford', 'Brighton');
myArray;

//When push() is used, the return value is the length of the array
let newLength = myArray.push('Bristol');
myArray;
newLength;

//pop() removes the last item of the array
myArray.pop();

//When pop() is used, the return value is the value the was removed
let removedItem = myArray.pop();
myArray;
removedItem;

//unshift() inserts a value into the front of an array
myArray.unshift('Edinburgh');
myArray;

//shift() removes the value in the front of the array
let removedItem2 = myArray.shift();
myArray;
removedItem;


//Example code 1

var list = document.querySelector('.output ul');
var totalBox = document.querySelector('.output p');
var total = 0;
list.innerHTML = '';
totalBox.textContent = '';

var products = ['Underpants:6.99',
 'Socks:5.99',
 'T-shirt:14.99',
 'Trousers:31.99',
 'Shoes:23.99'];

for(var i = 0; i < products.length; i++) {
 var subArray = products[i].split(':');
 var name = subArray[0];
 var price = Number(subArray[1]);
 total += price;
 itemText = name + ' — $' + price;

 var listItem = document.createElement('li');
 listItem.textContent = itemText;
 list.appendChild(listItem);
}

totalBox.textContent = 'Total: $' + total.toFixed(2);

//Example code 2

var list = document.querySelector('.output ul');
var searchInput = document.querySelector('.output input');
var searchBtn = document.querySelector('.output button');

list.innerHTML = '';

var myHistory= [];

searchBtn.onclick = function() 
{
    if(searchInput.value !== '') 
    {
        myHistory.unshift(searchInput.value);

        list.innerHTML = '';

        for(var i = 0; i < myHistory.length; i++) 
        {
            itemText = myHistory[i];
            var listItem = document.createElement('li');
            listItem.textContent = itemText;
            list.appendChild(listItem);
        }

        if(myHistory.length >= 5) 
        {
            myHistory.pop();
        }

        searchInput.value = '';
        searchInput.focus();
    }
}