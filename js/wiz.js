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

    let wizGold = getVar("wizGold");
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
    let locations = {
        "tower": "You travel to your modest one-story wizard tower.",
        "village": "You travel to the village 100 yds upwind from your tower.",
        "forest": "You head out into the forest behind your tower.",
        "mountain": "You head to the mountain above the forest."
    };
    let currentLocation = getLocation();
    if (newLocation == currentLocation) {
        report("You are already in " + currentLocation + ", silly wizard.");
    } else if (locations.hasOwnProperty(newLocation)) {
        report(locations[newLocation]);
        setLocation(newLocation);
    } else {
        report("I don't know where " + newLocation + " is.");
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
    if (currentLocation == "tower") {
        if (currentLibrary > currentSkill) {
            currentSkill = currentSkill + 1;
            setSkill(currentSkill);
            report("What a good student!");
        } else {
            report("You need a bigger library to increase your skill!");
        }
    } else {
        report("You can only study in the tower.");
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
    let currentGold = getVar("wizGold");
    let currentLibrary = getLibrary();
    if (currentLocation == "village"){
        // check if i have enough gold
        if (currentGold >= currentLibrary) {
            // if enough gold subtract enough to buy book
            currentGold -= currentLibrary;
            setGold(currentGold);
            // increase library upon purchase
            currentLibrary += 1;
            setLibrary(currentLibrary);
            report("You bought a book!");
            // not enough gold? msg w/ snark
        } else if (currentGold == 0) {
            report("Your wallet is empty. You're broke!");
        } else {
            report("You need more money to improve your library!");
        }

    } else {
        report("You can only shop in the village.");
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
    let currentGold = getVar("wizGold");
    let currentSkill = getSkill();
    if (currentLocation == "village") {
        currentGold += currentSkill;
        setGold(currentGold);

        if (currentSkill == 0) {
            report("You need to learn some magic! Read a book!");
        } else if (currentSkill >= 1 && currentSkill <= 3) {
            report("You perform some cute magics for the children.");
        } else if (currentSkill >= 4 && currentSkill <= 6) {
            report("You cast healing spells. How novel.");
        } else {
            report("You show off your mighty magics and everyone is impressed!");
        }
    
        
    } else {
        report("You can only work in the village.");
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

function getVar(varName) {
    let defaults = {
        "wizGold": 0
    };
    // is varName in defaults?
    if (! defaults.hasOwnProperty(varName)) {
        // if no then exit function
        return null; 
    }
    // continue and create new variable "response" that looks in localStorage for varName
    let response = localStorage.getItem(varName);
    // if it's not there we will get the default from the variable "defaults", add to localStorage, 
    // and set response to default and set response to equal the new value
    if (response === null){
        let value = defaults[varName];
        localStorage.setItem(varName, value);
        response = value;
        // if not null then continue
    }
    // is defaults[varName] an int? the string "number" is included with the builtin typeof
    if (typeof defaults[varName] === "number") {
    // checks to see if defaults is specifically a number 
        response = parseInt(response);
    }
    return response;
}

function setGold(wizGold) {
    localStorage.setItem("wizGold", wizGold);
    updateText();
}

function gather() {
    let currentLocation = getLocation();
    let currentIngredients = getIngredients();
    if (currentLocation == "forest") {
        currentIngredients += 1;
        setIngredients(currentIngredients);
        report("You gather your ingredients!");
    } else {
        report("You can only gather in the forest, silly wizard.");
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

function report(message) {
    let msg = document.getElementById("msg");
    msg.innerHTML = message;

}