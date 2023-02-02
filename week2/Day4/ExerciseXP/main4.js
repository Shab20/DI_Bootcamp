function changeEnough(itemprice, amountofchange){

    const sum = calculateSum(amountofchange)
    if(sum > itemprice){
        console.log("you can afford it")
        return true
    } else {
        console.log("you cannot afford it")
        return false
    }
    }
    
    function calculateSum(arr) {
        let sum = 0
        for (let i =0;i < arr.length;i++){
            let coinValue
            const numberofCoins = arr[i]
            if(i ===0){coinValue = 0.25}
            if(i ===1){coinValue = 0.20}
            if(i ===2){coinValue = 0.05}
            if(i ===3){coinValue = 0.01}
    console.log("we have", numberofCoins, "coins that have a value of", coinValue)
    
    sum = sum + numberofCoins * coinValue
    
        }
        console.log("the total sum is", sum)

        return sum
    }
    calculateSum([25,20,5,0])