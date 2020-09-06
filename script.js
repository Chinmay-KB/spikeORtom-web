function myfunction() {
    document.getElementById("excuse").innerHTML = "Loading";
    const Url = 'http://34.121.79.151/getx/';
    const othePram = {
        headers: {
            "content-type": "application/json; charset=UTF-8"
        },
        method: "GET"
    };
    fetch(new URL(Url))
        .then(data => data.json())
        .then(res => {
            document.getElementById("excuse").innerHTML = res.MESSAGE;
        });

}

function longLoad() {
    document.getElementById("excuse").innerHTML = "Loading";

    const Url = 'http://34.121.79.151/excuse/gen';
    const othePram = {
        headers: {
            "content-type": "application/json; charset=UTF-8"
        },
        method: "GET"
    };
    fetch(new URL(Url))
        .then(data => data.json())
        .then(res => {
            console.log(res);
            document.getElementById("excuse").innerHTML = res.excuses[0];

        });

}