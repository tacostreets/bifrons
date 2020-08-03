function main() {
    form = document.getElementById("wizard-form");
    form.addEventListener("submit", task);
    updateLocationText();
    updateSkillText();
}

function task(evt) {
    evt.preventDefault();
    text = document.getElementById("task").value;
    if (text == "study"){
        // do study action
        study();
    } else if (text == "reset") {
        resetWizard();
        updateLocationText();
        updateSkillText();
    } else {
        travel(text);
    }
}

function travel(newLocation) {//gets location and loops conditions to send a travel msg
    //replaces updateLocationText()
    currentLocation = getLocation();
    msg = document.getElementById("msg");
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
    wizLocation = localStorage.getItem("wizLocation");
    if (wizLocation === null) {
        setLocation("tower");
    }
    return localStorage.getItem("wizLocation");  
}

function setLocation(wizLocation) { //sets & stores location
    // local storage set here and can be changed inside this function later
    // location progress is set here locally 
    localStorage.setItem("wizLocation", wizLocation);//save
    updateLocationText();
}

function updateLocationText() { // creates variable and updates web page text
    wizLocation = getLocation();//created wizLocation variable
    p = document.getElementById("location");//pulls location from the form
    p.innerHTML = "<b>Your current location is " + wizLocation + ".</b>";//declares current location
}

function study() {
    currentLocation = getLocation();
    currentSkill = getSkill();
    msg = document.getElementById("msg");
    if (currentLocation == "tower") {
        currentSkill = currentSkill + 1;
        setSkill(currentSkill);
        msg.innerHTML = "What a good student!";
    } else {
        msg.innerHTML = "You can only study in the tower.";
    }
}

function getSkill() { //gets skill level
    // retrieves the skill level from localStorage or sets to 0 if there is no history
    wizSkill = localStorage.getItem("wizSkill");
    if (wizSkill === null) {
        setSkill(0);
    }
    wizSkill = localStorage.getItem("wizSkill");
    wizSkill = parseInt(wizSkill);
    return wizSkill;
}

function setSkill(wizSkill) { //sets & stores skill
    // sets and stores the skill aquired in the process of playing the game
    localStorage.setItem("wizSkill", wizSkill);
    updateSkillText();
}

function updateSkillText() {// creates variable and updates web page text
    wizSkill = getSkill();
    p = document.getElementById("skill");
    p.innerHTML = "Current skill level is " + wizSkill + ".";  
}

function resetWizard() {
    localStorage.clear();
}