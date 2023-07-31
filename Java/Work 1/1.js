Math.round
let user_input = Number.parseInt(prompt('Введите температуру в градусах Цельсия'));
alert(`Цельсия: ${user_input}\nФаренгейт: ${Math.round((9 / 5) * user_input + 32)}`)