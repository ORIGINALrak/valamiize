async function getAllCheck() {
    let response = await fetch("http://localhost:8080/checks/",
        {
            method: "GET"
        })

    let data = await response.json()
    console.log(data)

    document.getElementById('main').innerHTML = JSON.stringify(data)

}

function createCheck(GUID) {
    let response = fetch("http://localhost:8080/checks/",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "uuid": GUID,
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

function updateById(GUID) {
    let response = fetch(`http://localhost:8080/checks/${GUID}`,
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