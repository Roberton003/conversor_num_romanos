function convertToRoman() {
  var number = document.getElementById("number").value;
  var roman = "";
  var decimalValue = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  var romanNumeral = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I",
  ];

  if (isNaN(number) || number < 1 || number > 3999) {
    document.getElementById("result").style.color = "red";
    document.getElementById("result").innerHTML =
      "Por favor, digite um número entre 1 e 3999.";
    return;
  }

  for (var i = 0; i < decimalValue.length; i++) {
    while (decimalValue[i] <= number) {
      roman += romanNumeral[i];
      number -= decimalValue[i];
    }
  }

  document.getElementById("result").style.color = "red";
  document.getElementById("result").innerHTML = roman;
}

  