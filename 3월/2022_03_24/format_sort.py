#왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<5} | '.format('left', 'a')
print(s9)

#오른쪽 정렬
s10 = 'this is {0:>10} | done {1:>5} | '.format('left', 'a')
print(s10)

#가운데 정렬
s11 = 'this is {0:^10} | done {1:^5} | '.format('left', 'a')
print(s11)

#왼쪽정렬
s12 = 'this is {0:-<10} | done {1:o<5} | '.format('left', 'a')
print(s12)

#오른쪽 정렬
s13 = 'this is {0:+>10} | done {1:0>5} | '.format('right', 'b')
print(s13)

#가운데 정렬
s14 = 'this is {0:.^10} | done{1:@^5} | '.format('center', 'c')
print(s14)


