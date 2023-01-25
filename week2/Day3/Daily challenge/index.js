const maxNumber=6
let stars=""
for (let i = 0; i < maxNumber; i ++){
    stars = stars + "*"
    console.log(stars)
}

let arr = [
    ["*", "**"],
    ["***", "****"],
    ["*****", "******"],
  ];
  
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      console.log(arr[i][j]);
    }
  }