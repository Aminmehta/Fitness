def stats (a):
    workout= []
    for i in range (a):
        y= float(input("Enter the number of minutes you worked out on day"+ str((i+1))+":"))
        workout.append(y)
    average= sum(workout) / len(workout)
    maxN= max(workout)
    minN= min(workout)
    MaxDay= workout.index(maxN) + 1
    MinDay= workout.index(minN) + 1
    w= [average, MaxDay, MinDay]
    return w

nworkout = int(input("Number of days you worked out: "))
w= stats(nworkout)

print("Maximum minutes worked out on day", w[1])
print("Minimum minutes worked out on day",w[2])
avg=w[0]
print("Average miniutes worked out",w[0])
if avg < 30:
    print("you are working out less")
elif avg >= 30 and avg < 45:
    print("You are working out well")
elif avg > 45 and avg <120:
    print("You are doing very well")
elif avg >120:
    print("Dont try to hard")

