let count = Int(readLine()!)!

for _ in 1...count {
    let parenthesisString = readLine()!
    var pCount = 0
    
    for i in parenthesisString {
        if i == "(" {
            pCount += 1
        }

        else if i == ")" {
            pCount -= 1
            if pCount < 0 { break }
        }
    }

    print(pCount == 0 ? "YES" : "NO")
}
