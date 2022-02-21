let rus_name_of_building = ["Ферма","Дом","Шахта","Лесопилка","Дом лекаря","Дом инженеров","Хижина Шамана","Призвать в армию","Ничего не делать","",""];

let name_of_resource = ['food', 'people', 'stone', 'wood', 'army', 'farm', 'house', 'mine', 'sawmill', 'heal', 'engineer', 'shaman'];
let name_of_parametr = ["number_of_food","number_of_people","number_of_stone","number_of_wood", "number_of_army",
                        "number_of_grow_food","number_of_grow_people","number_of_grow_stone","number_of_grow_wood",
                        "number_of_farms","number_of_houses","number_of_mines","number_of_sawmills","number_of_healers","number_of_engins","number_of_shamans"]
let resources = {
    stone: 100,
    wood: 100,
    food: 3500,
    people: 100,
    mine: 0,
    sawmill: 0,
    farm: 0,
    house: 0,
    heal: 0,
    engineer: 0,
    shaman: 0,
    army: 0,
};


var player_choice = 8;
var day = 1;
var event_mod = 0;
var exit_code = 0;
//Забейте на эту часть кода, нужен, что бы с самого старта правильно показать ресурсы
for(var i = 0; i < 5; i++){ // Заполняем количество ресов
    document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]];
}
for(var i = 5; i < 9; i++){ // Заполняем прирост ресов
    if(i === 5){
        document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 5;
    }
    if(i === 6){
        document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 3;
    }
    if(i === 7){
        document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 2;
    }
    if(i === 8){
        document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 4;
    }

}
for(var i = 9; i < 16; i++){ // Заполняем количество зданий
    document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i - 4]];
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}




function new_choice1(){ // Функции для кнопок выбора новой постройки(Одни костыли +-)
    player_choice = 0;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice2(){
    player_choice = 1;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice3(){
    player_choice = 2;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice4(){
    player_choice = 3;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice5(){
    player_choice = 4;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice6(){
    player_choice = 5;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice7(){
    player_choice = 6;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice8(){
    player_choice = 7;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice9(){
    player_choice = 8;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice10(){
    player_choice = 9;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}
function new_choice11(){
    player_choice = 10;
    document.getElementById("show_choice").textContent = rus_name_of_building[player_choice];
}


function new_day(){
    if(exit_code === 0) {
        day++;
        let div = document.createElement('div');
        switch (player_choice) {
            case 0:
                if (resources["stone"] >= 15 && resources["wood"] >= 15) {
                    resources["stone"] -= 15;
                    resources["wood"] -= 15;
                    resources['farm']++;
                    div.innerHTML = "Мы успешно построили ферму, Милорд";
                } else {
                    div.innerHTML = "Кажется на ферму нет ресурсов, Милорд";
                }
                break;
            case 1:
                if (resources["stone"] >= 10 && resources["wood"] >= 10) {
                    resources["stone"] -= 10;
                    resources["wood"] -= 10;
                    resources['house']++;
                    div.innerHTML = "Мы успешно построили дом, Милорд";
                } else {
                    div.innerHTML = "Кажется на дом нет ресурсов, Милорд";
                }
                break;
            case 2:
                if (resources["stone"] >= 20 && resources["wood"] >= 10) {
                    resources["stone"] -= 20;
                    resources["wood"] -= 10;
                    resources['mine']++;
                    div.innerHTML = "Мы успешно построили шахту, Милорд";
                } else {
                    div.innerHTML = "Кажется на шахту нет ресурсов, Милорд";
                }
                break;
            case 3:
                if (resources["stone"] >= 10 && resources["wood"] >= 20) {
                    resources["stone"] -= 10;
                    resources["wood"] -= 20;
                    resources['sawmill']++;
                    div.innerHTML = "Мы успешно построили лесопилку, Милорд";
                } else {
                    div.innerHTML = "Кажется на лесопилку нет ресурсов, Милорд";
                }
                break;
            case 4:
                if (resources["stone"] >= 15 && resources["wood"] >= 15) {
                    resources["stone"] -= 15;
                    resources["wood"] -= 15;
                    resources['heal']++;
                    div.innerHTML = "Мы успешно построили дом для лекаря, Милорд";
                } else {
                    div.innerHTML = "Кажется на дом для лекаря нет ресурсов, Милорд";
                }
                break;
            case 5:
                if (resources["stone"] >= 30 && resources["wood"] >= 20) {
                    resources["stone"] -= 30;
                    resources["wood"] -= 20;
                    resources['engineer']++;
                    div.innerHTML = "Мы успешно построили дом для инженеров, Милорд";
                } else {
                    div.innerHTML = "Кажется на дом для инженеров нет ресурсов, Милорд";
                }
                break;
            case 6:
                if (resources["stone"] >= 10 && resources["wood"] >= 30) {
                    resources["stone"] -= 10;
                    resources["wood"] -= 30;
                    resources['shaman']++;
                    div.innerHTML = "Мы успешно построили хижину для шамана, Милорд";
                } else {
                    div.innerHTML = "Кажется на хижину для шамана нет ресурсов, Милорд";
                }
                break;
            case 7:
                var number_of_soldiers = parseInt(prompt("Сколько солдат вы хотите, Милорд?"));
                if (number_of_soldiers * 4 <= resources["food"] && number_of_soldiers * 1 <= resources["stone"] && number_of_soldiers * 2 <= resources["wood"]) {
                    resources["stone"] -= number_of_soldiers * 1;
                    resources["wood"] -= number_of_soldiers * 2;
                    resources["food"] -= number_of_soldiers * 4;
                    resources["people"] -= number_of_soldiers;
                    resources["army"] += number_of_soldiers;
                    div.innerHTML = "Мы успешно призвали " + number_of_soldiers + " в армию, Милорд";
                } else {
                    div.innerHTML = "Кажется у нас нет столько ресурсов для армии, Милорд";
                }
                break;
            case 8:
                div.innerHTML = "Решили взять отдых, Милорд?";
                break;

        }

        div.innerHTML += "<br>";
        var event = getRandomInt(7);
        var luck = getRandomInt(101);
        var unluck = getRandomInt(51);
        unluck += event_mod;
        switch (event) { //Ивенты
            case 0: //Хворь
                unluck -= resources["heal"] * 10;
                if (luck >= unluck) {
                    div.innerHTML += "Город поразила хворь, но наши лекари сумели с ней справиться";
                } else {
                    var minus = Math.max(Math.min(Math.round((unluck - luck - getRandomInt(31)) / 100 * (resources['people'] + resources["army"])), (resources["people"] + resources["army"])), 1);
                    var minus_army = Math.max(Math.round(minus * getRandomInt(101) / 100), resources['army']);
                    var minus_people = minus - minus_army;
                    resources['people'] -= minus_people;
                    resources['army'] -= minus_army;
                    div.innerHTML += "Город поразила хворь, наши лекари были не в силах всем помочь, погибло " + minus + " человек";
                }
                break;
            case 1: //Непогода
                unluck -= resources["shaman"] * 10;
                var chances_for_good_end = Math.max(Math.min(resources["shaman"] - 40, 20), 0);
                if(luck <= chances_for_good_end){
                    div.innerHTML += "Боги были злы на нас и хотели уничтожить урожай, но наши шаманы смогли их успокоить и <strong>даже задобрить их</strong>";
                    event_mod -= 30;
                }
                else if (luck >= unluck) {
                    div.innerHTML += "Боги были злы на нас и хотели уничтожить урожай, но наши шаманы смогли их успокоить";
                } else {
                    var minus = Math.min(Math.round((unluck - luck) * (resources['food'] / ((getRandomInt(10) + 3) * 1000))), resources["food"]);
                    resources['food'] -= minus;
                    div.innerHTML += "Боги не могут больше терпеть наше поведение, они забрали у нас " + minus + " еды";
                }
                break;
            case 2: //Лавина
                unluck -= resources["engineer"] * 10;
                if (luck >= unluck) {
                    div.innerHTML += "В городе произошло землетрясение, но укрепления, которые построили инженеры, спасли все строения";
                } else {
                    var choose = getRandomInt(8) + 5;
                    var minus = Math.max(Math.round(getRandomInt(resources[name_of_resource[choose]]) * (Math.max(50 - (unluck - luck), 0) + getRandomInt(31)) / 100) , 1);
                    if(minus <= resources[name_of_resource[choose]]){
                        resources[name_of_resource[choose]] -= minus;
                        div.innerHTML += "В городе произошло землетрясение, которое уничтожило " + minus + " &quot;" + rus_name_of_building[choose - 5] + "&quot; ";
                    } else {
                        div.innerHTML += "В городе произошло землетрясение, но к счастью, оно произошло на пустыре";
                    }
                }
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
                break;
            case 6:
                break;

        }
        document.getElementById("space_for_message").append(div);
        document.getElementById("space_for_message").scrollTop = Number.MAX_SAFE_INTEGER;
        for (var i = 0; i < 5; i++) { // Заполняем количество ресов
            if (i === 0) {
                resources['food'] -= resources['people'];
                resources['food'] -= Math.round(resources['army'] / 3);
                resources['food'] += resources['farm'] * 5;
            }
            if (i === 1 && resources['people'] !== 0) {
                resources['people'] += resources['house'] * 3;
            }
            if (i === 2) {
                resources['stone'] += resources['mine'] * 2;
            }
            if (i === 3) {
                resources['wood'] += resources['sawmill'] * 4;
            }
            document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]];


        }
        for (var i = 5; i < 9; i++) { // Заполняем прирост ресов
            if (i === 5) {
                document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 5;
            }
            if (i === 6) {
                document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 3;
            }
            if (i === 7) {
                document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 2;
            }
            if (i === 8) {
                document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i]] * 4;
            }

        }
        for (var i = 9; i < 16; i++) { // Заполняем количество зданий
            document.getElementById(name_of_parametr[i]).textContent = resources[name_of_resource[i - 4]];
        }

        if (resources["people"] + resources["army"] <= 0) {
            alert('*В городе умерли все. Смерть вашего помощника стала последней каплей, которая сломала вашу нервную систему. Вы закончили жизнь самоубийством*');
            exit_code = 1;
        }
        if (resources["food"] <= 0) {
            alert('К сожалению, голодным жителям безразницы, что у вас в руках. Боюсь, что через 10 минут вы будете съедены, Милорд. Это конец вашей истории');
            exit_code = 1;
        }
        document.getElementById("number_of_days").textContent = day + ' ';
        let end = document.createElement('div');
        end.innerHTML = "ДЕНЬ " + day;
        document.getElementById("space_for_message").append(end);
        document.getElementById("space_for_message").scrollTop = Number.MAX_SAFE_INTEGER;
        event_mod += getRandomInt(6);
    }}