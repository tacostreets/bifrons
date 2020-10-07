function main() {
    let form = document.getElementById("wizard-form");
    form.addEventListener("submit", task); // enter or click submit and task function is called with evt passed thru
    updateText();
    
}

function task(evt) { // submit is the event and the task is the object evt 
    evt.preventDefault(); // submit default is to reload page w/ form params - this prevents reloading the page
    let text = document.getElementById("task").value; //manually access task input field and update relevant parts in the page
    if (text == "study"){
        // do study action
        study();
    } else if (text == "work"){
        work();
    } else if (text == "shop"){
        shop();
    } else if (text == "gather"){
        gather();
    } else if (text == "reset") { //update back to zero
        resetWizard();
        updateText();
    } else {
        travel(text); //passes thru the travel input, calls the function, sets the funtion and updates text
    } 
}
function updateText() {
    let p = 0;
    function nouns(noun, num) {
        if (num == 1) {
            return "" + num + " " + noun 
        } else {
            return "" + num + " " + noun + "s"
        } 
    }

    let wizLocation = getLocation();//created wizLocation variable
    p = document.getElementById("location");//pulls location from the form
    p.innerHTML = "<b>Your current location is " + wizLocation + ".</b>";//declares current location

    let wizSkill = getSkill();
    p = document.getElementById("skill");
    p.innerHTML = "Current skill level is " + wizSkill + "!"; 

    let wizGold = getGold();
    p = document.getElementById("gold");
    p.innerHTML = "You now have " + nouns("coin", wizGold) + "!";

    let wizLibrary = getLibrary();
    p = document.getElementById("library");
    p.innerHTML = "You now have " + nouns("book", wizLibrary) + "!";

    let wizIngredients = getIngredients();
    p = document.getElementById("ingredients");
    p.innerHTML = "You now have " + nouns("ingredient", wizIngredients) + "!";
}

function travel(newLocation) {//gets location and loops conditions to send a travel msg
    //replaces updateLocationText()
    let currentLocation = getLocation();
    let msg = document.getElementById("msg");
    if (newLocation == currentLocation) {
        msg.innerHTML = "You are already in " + currentLocation + ", silly wizard.";
    } else if (newLocation == "tower") {
        msg.innerHTML = "You travel to your modest one-story wizard tower.";
        setLocation(newLocation);
    } else if (newLocation == "village") {
        msg.innerHTML = "You travel to the village 100 yds upwind from your tower.";
        setLocation(newLocation);
    } else if (newLocation == "forest") {
        msg.innerHTML = "You head out into the forest behind your tower.";
        setLocation(newLocation);
    } else {
        msg.innerHTML = "I don't know where " + newLocation + " is.";
    }
}

function getLocation() { //gets location from storage
    // retrieves the location from entry in the localStorage
    let wizLocation = localStorage.getItem("wizLocation");
    if (wizLocation === null) {
        setLocation("tower");
    }
    return localStorage.getItem("wizLocation");  
}

function setLocation(wizLocation) { //sets & stores location
    // local storage set here and can be changed inside this function later
    // location progress is set here locally 
    localStorage.setItem("wizLocation", wizLocation);//save
    updateText();
}

function study() {
    let currentLocation = getLocation();
    let currentSkill = getSkill();
    let currentLibrary = getLibrary();
    let msg = document.getElementById("msg");
    if (currentLocation == "tower") {
        if (currentLibrary > currentSkill) {
            currentSkill = currentSkill + 1;
            setSkill(currentSkill);
            msg.innerHTML = "What a good student!";
        } else {
            msg.innerHTML = "You need a bigger library to increase your skill!";
        }
    } else {
        msg.innerHTML = "You can only study in the tower.";
    }
}

function getSkill() { //gets skill level
    // retrieves the skill level from localStorage or sets to 0 if there is no history
    let wizSkill = localStorage.getItem("wizSkill");
    if (wizSkill === null) {
        setSkill(0);
    }
    wizSkill = localStorage.getItem("wizSkill");
    wizSkill = parseInt(wizSkill); // local storage always stores as a string so convert to int
    return wizSkill;
}

function setSkill(wizSkill) { //sets & stores skill
    // sets and stores the skill aquired in the process of playing the game
    localStorage.setItem("wizSkill", wizSkill);
    updateText();
}

function shop() {
    let currentLocation = getLocation();
    let currentGold = getGold();
    let currentLibrary = getLibrary();
    let msg = document.getElementById("msg");
    if (currentLocation == "village"){
        // check if i have enough gold
        if (currentGold >= currentLibrary) {
            // if enough gold subtract enough to buy book
            currentGold -= currentLibrary;
            setGold(currentGold);
            // increase library upon purchase
            currentLibrary += 1;
            setLibrary(currentLibrary);
            msg.innerHTML = "You bought a book!";
            // not enough gold? msg w/ snark
        } else if (currentGold == 0) {
            msg.innerHTML = "Your wallet is empty. You're broke!"
        } else {
            msg.innerHTML = "You need more money to improve your library!"
        }

    } else {
        msg.innerHTML = "You can only shop in the village.";
    }
}

function getLibrary() {
    let wizLibrary = localStorage.getItem("wizLibrary");
    if (wizLibrary === null) {
        setLibrary(1);
    }
    wizLibrary = localStorage.getItem("wizLibrary");
    wizLibrary = parseInt(wizLibrary);
    return wizLibrary;
}

function setLibrary(wizLibrary) {
    localStorage.setItem("wizLibrary", wizLibrary);
    updateText();
}

function work() { // 
    let currentLocation = getLocation();
    let currentGold = getGold();
    let currentSkill = getSkill();
    let msg = document.getElementById("msg");
    if (currentLocation == "village") {
        currentGold += currentSkill;
        setGold(currentGold);

        if (currentSkill == 0) {
            msg.innerHTML = "You need to learn some magic! Read a book!";
        } else if (currentSkill >= 1 && currentSkill <= 3) {
            msg.innerHTML = "You perform some cute magics for the children.";
        } else if (currentSkill >= 4 && currentSkill <= 6) {
            msg.innerHTML = "You cast healing spells. How novel.";
        } else {
            msg.innerHTML = "You show off your mighty magics and everyone is impressed!";
        }
    
        
    } else {
        msg.innerHTML = "You can only work in the village.";
    }

} 

function getGold() {
    let wizGold = localStorage.getItem("wizGold");
    if (wizGold === null) {
        setGold(0);
    }
    wizGold = localStorage.getItem("wizGold");
    wizGold = parseInt(wizGold);
    return wizGold;
}

function setGold(wizGold) {
    localStorage.setItem("wizGold", wizGold);
    updateText();
}

function gather() {
    let currentLocation = getLocation();
    let currentIngredients = getIngredients();
    let msg = document.getElementById("msg");
    if (currentLocation == "forest") {
        currentIngredients += 1;
        setIngredients(currentIngredients);
        msg.innerHTML = "You gather your ingredients!";
    } else {
        msg.innerHTML = "You can only gather in the forest, silly wizard.";
    }
}

function getIngredients() {
    let wizIngredients = localStorage.getItem("wizIngredients");
    if (wizIngredients === null) {
        setIngredients(0);
    }
    wizIngredients = localStorage.getItem("wizIngredients");
    wizIngredients = parseInt(wizIngredients);
    return wizIngredients;
}

function setIngredients(wizIngredients) {
    localStorage.setItem("wizIngredients", wizIngredients);
    updateText();
}

function resetWizard() {
    localStorage.clear();
}