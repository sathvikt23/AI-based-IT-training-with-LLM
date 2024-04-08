

const axios = require("axios");
let i;
let no = 2421200;
async function lol() {
 for(i=0;i<20;i++){
    no+=1;
    try {
        const response = await axios.post("http://teleuniv.in/netra/api.php", {
            method: "32",
            rollno: no
        }).then((response)=>{

        console.log(response.data.hallticketno);
        if(response.data.hallticketno==="21bd1a050k"){
            console.log("found")
            
        }
    })
    } catch (error) {
        console.error(error);
    }
}
}

lol();
