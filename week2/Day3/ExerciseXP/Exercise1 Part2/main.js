const people = ["Greg", "Mary", "Devon", "James"];

people.splice(people.indexOf("Greg"), 1);
people[people.indexOf("James")] = "Jason";
people.push("Shab");
console.log(people.indexOf("Mary"));
const copy = people.slice(1, people.length-1);
console.log(people.indexOf("Foo"));
const last = people[people.length - 1];

console.log("people array:",people);
console.log("copy array:",copy);
console.log("last element:",last);

// Iterate through the people array and console.log each person
console.log("Iterating through people array and console.log each person:")
people.forEach(person => console.log(person));

// Iterate through the people array and exit the loop after console.logging "Jason"
console.log("Iterating through the people array and exit the loop after console.logging 'Jason':")
people.some(person => {
    console.log(person);
    return person === "Jason";
});
