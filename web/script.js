var guids = [];

async function getAllCheck() {
    let response = await fetch("http://localhost:8080/checks/",
        {
            method: "GET"
        })

    let data = await response.json()
    console.log(data)

    document.getElementById('main').innerHTML = JSON.stringify(data)

}

function createCheck() {
    let guid = randomguid();
    let response = fetch("http://localhost:8080/checks/",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "uuid": guid,
                "name": "sum_is_zero",
                "version": "0.0.1",
                "released": "2025-01-09T10:21:25.886279",
                "description": "Checks if the sum of the amounts is equal to zero.",
                "lang": "python",
                "params": [
                    "amount_1: int",
                    "amount_2: int",
                    "amount_3: int"
                ],
                "func_body": "return (amount_1 + amount_2 + amount_3) == 0"
            })
        },
    )
    guids.push(guid);
}

async function getById(GUID) {
    let response = await fetch(`http://localhost:8080/checks/${GUID}`,
        {
            method: "GET"
        })

    let data = await response.json()
    console.log(data)

    document.getElementById('main').innerHTML = JSON.stringify(data)

}

function deleteById(GUID) {
    let response = fetch(`http://localhost:8080/checks/${GUID}`,
        {
            method: "DELETE",
            headers: {
        }
    })
}

function updateById() {
    let response = fetch(`http://localhost:8080/checks/${GUID}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "uuid": randomguid(),
                "name": "sum_is_valami",
                "version": "9.9.9",
                "released": "tegnap",
                "description": "valami.",
                "lang": "python",
                "params": [
                    "amount_1: int",
                    "amount_2: int",
                    "amount_3: int"
                ],
                "func_body": "return (amount_1 + amount_2 + amount_3) == 0"
        })
    })
}

function randomguid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
    .replace(/[xy]/g, function (c) {
        const r = Math.random() * 16 | 0, 
            v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

async function getAllProcedures() {
    let response = await fetch("http://localhost:8080/procedures/",
        {
            method: "GET"
        })

    let data = await response.json()
    console.log(data)

    document.getElementById('main').innerHTML = JSON.stringify(data)

}

function createProcedure() {
function waioawduihioawdawdw() {
    let anyád = []
    for(let i = 0; i < guids.length; i++)
    {
        anyád.push('<a href="getById(guids[i])">' + guids[i] + '</a>');
    }
    return anyád;
}

async function createProcedure() {
    let response = await fetch("http://localhost:8080/procedures/",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "uuid": randomguid(),
                "name": "some_fancy_name",
                "version": "0.0.1",
                "description": "The scope of this procedure is defined by some theory about how to validate related data.",
                "checks": waioawduihioawdawdw(), 
            })
        },
    )
    document.getElementById('procedure').innerHTML = JSON.stringify(response)
    guids = [];
}


async function getProcedureById(GUID) {
    let response = await fetch(`http://localhost:8080/procedures/${GUID}`,
        {
            method: "GET"
        })

    let data = await response.json()
    console.log(data)

    document.getElementById('main').innerHTML = JSON.stringify(data)

}

function deleteProcedureById(GUID) {
    let response = fetch(`http://localhost:8080/procedures/${GUID}`,
        {
            method: "DELETE",
            headers: {
        }
    })
}

function updateProcedureById(GUID) {
    let response = fetch(`http://localhost:8080/procedures/${GUID}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "uuid": GUID,
                "name": "sum_is_valami",
                "version": "9.9.9",
                "released": "tegnap",
                "description": "valami.",
                "lang": "python",
                "params": [
                    "amount_1: int",
                    "amount_2: int",
                    "amount_3: int"
                ],
                "func_body": "return (amount_1 + amount_2 + amount_3) == 0"
        })
    })
}