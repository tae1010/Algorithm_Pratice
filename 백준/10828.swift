
var orderCount = Int(readLine()!)!\
\
for _ in 1...orderCount \{\
    var stackOrder = readLine()!.split(separator: " ").map\{String($0)\}\
    switch stackOrder[0] \{\
    case "push":\
        stack.append(Int(stackOrder[1])!)\
    case "pop":\
        if stack.isEmpty \{\
            print(-1)\
        \} else \{\
            print(stack.removeLast())\
        \}\
    case "size":\
        print(stack.count)\
    case "empty":\
        stack.isEmpty ? print(1) : print(0)\
    case "top":\
        stack.isEmpty ? print(-1) : print((stack.last)!)\
    default:\
    break\
    \}\
\}}
