const sentence = 'This movie is not that bad ! I like it'
const wordNot = sentence.search ('not')
const wordBad = sentence.search ('bad')

const firstPart = sentence.slice (0,wordNot)
const secondPart = sentence.slice(wordBad + 3)

console.log(firstPart + "good" + secondPart)

console.log('wordBad:', wordBad)
console.log('wordNot:', wordNot)