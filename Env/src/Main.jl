function main()
    mod = 2^4        
    a = 0
    N = 500000000
    for i in 0:N-1
        a+=i
        a%=mod
    end
    println(a)
end

main()