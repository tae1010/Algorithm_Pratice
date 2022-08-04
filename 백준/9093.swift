var count = Int(readLine()!)!

for _ in 1...count {
    let sentanse = readLine()!.split(separator: " ")
    var reverseSentanse = ""
    
    for i in sentanse {
        reverseSentanse += i.reversed() + " "
    }
}
