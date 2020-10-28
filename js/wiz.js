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

    let wizLocation = load("wizLocation");//created wizLocation variable
    p = document.getElementById("location");//pulls location from the form
    p.innerHTML = "<b>Your current location is " + wizLocation + ".</b>";//declares current location

    let wizSkill = load("wizSkill");
    p = document.getElementById("skill");
    p.innerHTML = "Current skill level is " + wizSkill + "!"; 

    let wizGold = load("wizGold");
    p = document.getElementById("gold");
    p.innerHTML = "You now have " + nouns("coin", wizGold) + "!";

    let wizLibrary = load("wizLibrary");
    p = document.getElementById("library");
    p.innerHTML = "You now have " + nouns("book", wizLibrary) + "!";

    let wizIngredients = load("wizIngredients");
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
    let currentLocation = load("wizLocation");
    if (newLocation == currentLocation) {
        report("You are already in " + currentLocation + ", silly wizard.");
    } else if (locations.hasOwnProperty(newLocation)) {
        report(locations[newLocation]);
        save("wizLocation", newLocation);
    } else {
        report("I don't know where " + newLocation + " is.");
    }
}

function study() {
    let currentLocation = load("wizLocation");
    let currentSkill = load("wizSkill");
    let currentLibrary = load("wizLibrary");
    if (currentLocation == "tower") {
        if (currentLibrary > currentSkill) {
            currentSkill = currentSkill + 1;
            save("wizSkill", currentSkill);
            report("What a good student!");
        } else {
            report("You need a bigger library to increase your skill!");
        }
    } else {
        report("You can only study in the tower.");
    }
}

function shop() {
    let currentLocation = load("wizLocation");
    let currentGold = load("wizGold");
    let currentLibrary = load("wizLibrary");
    if (currentLocation == "village"){
        // check if i have enough gold
        if (currentGold >= currentLibrary) {
            // if enough gold subtract enough to buy book
            currentGold -= currentLibrary;
            save("wizGold", currentGold);
            // increase library upon purchase
            currentLibrary += 1;
            save("wizLibrary", currentLibrary);
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

function work() { // 
    let currentLocation = load("wizLocation");
    let currentGold = load("wizGold");
    let currentSkill = load("wizSkill");
    if (currentLocation == "village") {
        currentGold += currentSkill;
        save("wizGold", currentGold);

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

function load(name) {
    let defaults = {
        "wizGold": 0,
        "wizIngredients": 0,
        "wizLibrary": 1,
        "wizSkill": 0,
        "wizLocation": "tower"
    };
    // is name in defaults?
    if (! defaults.hasOwnProperty(name)) {
        // if no then exit function
        return null; 
    }
    // continue and create new variable "response" that looks in localStorage for name
    let response = localStorage.getItem(name);
    // if it's not there we will get the default from the variable "defaults", add to localStorage, 
    // set response to default, and set response to equal the new value
    if (response === null){
        let value = defaults[name];
        localStorage.setItem(name, value);
        response = value;
        // if not null then continue
    }
    // is defaults[name] an int? the string "number" is included with the builtin typeof
    if (typeof defaults[name] === "number") {
    // checks to see if defaults is specifically a number 
        response = parseInt(response);
    }
    return response;
}

function save(name, value) {
    localStorage.setItem(name, value);
    updateText();
}

function setSkill(value) { 
    localStorage.setItem("wizSkill", value);
    updateText();
}

function gather() {
    let currentLocation = load("wizLocation");
    let currentIngredients = load("wizIngredients");
    if (currentLocation == "forest") {
        currentIngredients += 1;
        save("wizIngredients", currentIngredients);
        report("You gather your ingredients!");
    } else {
        report("You can only gather in the forest, silly wizard.");
    }
}

function resetWizard() {
    localStorage.clear();
}

function report(message) {
    let msg = document.getElementById("msg");
    msg.innerHTML = message;

}