function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){

        let eventTextElement = document.querySelector(".eventContent");
        let eventTextElement2 = document.querySelector(".eventContent2");

        for ( let i in data.result ){
            for ( let j in data.result[i] ){
            let spot = data.result[i][j];
            let spotImg = spot.file.split(/(?=http)/g);

            if ( j < 2 ){
                // 創造小div
                let divElement = document.createElement("div");
                divElement.classList.add("inner-div1");
                divElement.style.display = "flex";
                divElement.style.width = "auto";
    

                // 圖片放進小div
                let imgElement = document.createElement("img");
                imgElement.classList.add("spot-img1");
                imgElement.src = spotImg[0];
                imgElement.style.height = "50px";
                imgElement.style.width = "80px";
                divElement.appendChild(imgElement);

                // 標題放進小div
                let spanElement = document.createElement("span");
                spanElement.classList.add("spot-text1");
                spanElement.textContent = spot.stitle;
                spanElement.style.position = "relative";
                spanElement.style.top = "12px";
                spanElement.style.left = "7px";
                divElement.appendChild(spanElement);

                // 小div放進大div
                eventTextElement.appendChild(divElement);

            } else if ( j < 10 ){
                // 創造小div
                let divElement = document.createElement("div");
                divElement.classList.add("inner-div2");
                divElement.style.width = "auto";

                // 圖片放進小div
                let imgElement = document.createElement("img");
                imgElement.classList.add("spot-img2");
                imgElement.src = spotImg[0];
                divElement.appendChild(imgElement);

                // 標題放進小div
                let spanElement = document.createElement("div");
                spanElement.classList.add("spot-text2");
                spanElement.textContent = spot.stitle;
                divElement.appendChild(spanElement);

                // 小div放進大div
                eventTextElement2.appendChild(divElement);

            } else if ( j < 18 ){

            } else if ( j < 26 ){

            } else if ( j < 34 ){

            } else if ( j < 42 ){

            } else if ( j < 50 ){

            } else {

            }

            }
        }
    });
}

getData();
