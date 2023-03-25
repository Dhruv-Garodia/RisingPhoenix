let keyValuePairs = [];

function addKeyValuePair() {
  const key = document.getElementById("key").value;
  const value = document.getElementById("value").value;

  const pair = {
    key: key,
    value: value
  };

  keyValuePairs.push(pair);

  const keyValueList = document.getElementById("keyValueList");
  const listItem = document.createElement("li");
  listItem.innerText = `${key}: ${value}`;
  keyValueList.appendChild(listItem);

  document.getElementById("key").value = "";
  document.getElementById("value").value = "";
}

function clearKeyValuePairs() {
  keyValuePairs = [];
  const keyValueList = document.getElementById("keyValueList");
  keyValueList.innerHTML = "";
}

function submitKeyValuePairs() {
  const xhr = new XMLHttpRequest();
  const url = "http://localhost:3000/";

  xhr.open("POST", url);
  xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhr.send(JSON.stringify(keyValuePairs));
}