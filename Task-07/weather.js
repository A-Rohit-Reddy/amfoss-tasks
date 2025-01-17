const apiUrl="https://api.openweathermap.org/data/2.5/weather?units=metric&q=";
const apiKey="c2a1bde9915a9165c16e964529151b5a";

const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");

const weatherBackgrounds = {
    Clear: "images/clear.png",
    Clouds: "images/clouds.png",
    Rain: "images/rain.png",
    Snow: "images/snow.png",
    Thunderstorm: "images/thunderstorm.png",
    Mist: "images/mist.png",
    Haze: "images/haze.png",
    Fog: "images/fog.png"
};

const defaultBackground="images/error.png";

async function checkWeather(city_name){
    try{
        const response = await fetch(apiUrl + city_name + `&appid=${apiKey}`);

        var data = await response.json();

        console.log(data);
                

        document.querySelector(".city").innerHTML=data.name;
        document.querySelector(".temp").innerHTML=Math.round(data.main.temp) + "\u00B0C";
        document.querySelector(".point").innerHTML=data.weather[0].main;

        const weatherCondition = data.weather[0].main;
        const background = weatherBackgrounds[weatherCondition];
                  
        const card = document.querySelector(".card");
        card.setAttribute("style", `background-image: url(${background}); background-repeat: no-repeat; background-position: center; background-size: cover;`);
                
    } catch(error){
        const card = document.querySelector(".card");
        if (card) {
            card.setAttribute("style",`background-image: url(${defaultBackground}); color: transparent; background-position: top; background-size: 65% 85%;`);
        }      
    }
                
}    

searchBtn.addEventListener("click", ()=>{
    checkWeather(searchBox.value);
})

function getGreetingMessage() {
    const currentHour = new Date().getHours();

    if (currentHour >= 4 && currentHour < 12) {
        return "Good Morning!";
    } else if (currentHour >= 12 && currentHour < 17) {
        return "Good Afternoon!";
    } else if (currentHour >= 17 && currentHour < 22) {
        return "Good Evening!";
    } else {
        return "Good Night!";
    }
}

function displayGreeting() {
    const greetingMessage = getGreetingMessage();
    const greetingElement = document.createElement("h1");
    greetingElement.className = "greeting";
    greetingElement.innerText = greetingMessage;

    // Append the greeting to the card
    const weatherCard = document.querySelector(".card");
    weatherCard.prepend(greetingElement); // Add the greeting at the top of the card
}

// Call the function to display the greeting
displayGreeting();

