import random

# ==========================================
# 1. STATE MANAGEMENT (For Future[2.0])
# ==========================================
stats = {
    "User": {"runs": 0, "wickets": 0},
    "AI": {"runs": 0, "wickets": 0}
}

# ==========================================
# 2. USER/AI MOVE
# ==========================================
def get_user_move():
    while True:
        try:
            print("-" * 30)
            user_move = int(input("🏏 Your Turn (0-6): "))
            if 0 <= user_move <= 6:
                return user_move
            else:
                print("❌ Invalid! Enter a number between 0 and 6.")
        except ValueError:
            print("⚠️ Numbers only! Please enter a digit.")

def get_ai_move(mode, is_ai_batting):
    numbers = [0, 1, 2, 3, 4, 5, 6]
    
    if mode == 'easy':
        return random.randint(0, 6)
    elif mode == 'normal':
        weights = [1.5, 1.5, 1.5, 1, 1, 1, 1] # মিক্সড
        return random.choices(numbers, weights=weights)[0]
    elif mode == 'hard':
        if is_ai_batting:     
            weights = [3, 3, 3, 1, 1, 1, 1] 
        else:
            weights = [1, 1, 1, 1, 1, 4, 5] 
        return random.choices(numbers, weights=weights)[0]
    return random.randint(0, 6)

# ==========================================
# 3. TOSS SYSTEM
# ==========================================
def perform_toss():
    
    toss_choice = ''
    while toss_choice not in ['head', 'tail']:
        toss_choice = input('\nChoose Head or Tail: ').lower().strip()
        if toss_choice not in ['head', 'tail']:
            print("❌ Invalid choice!")

    random_toss = random.choice(['head', 'tail'])
    print(f"\n🪙  Toss Result: {random_toss.upper()}")

    if toss_choice == random_toss:
        print("✅ You won the Toss!")
        selection = ''
        while selection not in ['bat', 'bowl']:
            selection = input("Choose to 'Bat' or 'Bowl': ").lower().strip()
            if selection not in ['bat', 'bowl']:
                print("❌ Invalid choice!")
        
        return ('User', 'AI') if selection == 'bat' else ('AI', 'User')
        
    else:
        print("❌ You lost the toss!")
        ai_selection = random.choice(['bat', 'bowl'])
        print(f"🤖 AI decided to {ai_selection} first.")
        return ('AI', 'User') if ai_selection == 'bat' else ('User', 'AI')

# ==========================================
# 4. GAME ENGINE (Innings Logic)
# ==========================================
def play_innings(batting_player, bowling_player, target=None, mode ='easy'):
    print(f"\n{'*' * 10} {batting_player.upper()} IS BATTING {'*' * 10}")
    current_runs = 0
    current_wickets = 0
    max_wickets = 10  
    overs = 5
    total_balls = overs * 6
    balls_bowled = 0 

    while current_wickets < max_wickets and balls_bowled < total_balls:
        u_move = get_user_move()
        
        ai_is_batting = (batting_player == 'AI')
        a_move = get_ai_move(mode, ai_is_batting)

        balls_bowled += 1
        over_num = balls_bowled // 6
        ball_num = balls_bowled % 6

        print(f"\n📤 Moves: User [{u_move}] vs AI [{a_move}]")

        if u_move == a_move:
            print("💥 BOOM! IT'S AN OUT!")
            current_wickets += 1
        else:
            run_scored = u_move if batting_player == 'User' else a_move
            current_runs += run_scored
            print(f"✅ Safe! {run_scored} runs added.")

        print(f"📊 Score: {current_runs}/{current_wickets} | Over: {over_num}.{ball_num}")
        print(f"⏳ Balls Left: {total_balls - balls_bowled}")

        if target is not None: 
            print(f"🎯 Need {target - current_runs} more to win.")
            if current_runs >= target:
                print(f"\n🔥 Target reached by {batting_player}!")
                break

    return current_runs

# ==========================================
# 5. MAIN CONTROLLER
# ==========================================
def main():
    print("\n" + "="*40)
    print("      WELCOME TO HAND CRICKET v1.0      ")
    print("="*40)
    print("\nSelect Difficulty:")
    print("1. Easy | 2. Normal | 3. Hard")
    choice = input("Enter choice (1/2/3): ")
    
    modes = {'1': 'easy', '2': 'normal', '3': 'hard'}
    game_mode = modes.get(choice, 'easy')

    batter, bowler = perform_toss()
    
    score1 = play_innings(batter, bowler ,mode = game_mode)
    print(f"\n{'=' * 40}")
    print(f"🏁 END OF 1ST INNINGS")
    print(f"👉 {batter} scored {score1} runs.")
    print(f"{'=' * 40}")
    
    target = score1 + 1
    print(f"\n📢 TARGET: {target} runs in 5 overs.")
    
    score2 = play_innings(bowler, batter, target=target, mode = game_mode)
    
    print(f"\n" + "#" * 40)
    print("           FINAL MATCH RESULT           ")
    print("#" * 40)
    
    if score2 >= target:
        print(f"\n🏆 CONGRATULATIONS! {bowler.upper()} WON!")
    elif score2 == score1:
        print("\n🤝 MATCH DRAW!")
    else:
        print(f"\n🏆 CONGRATULATIONS! {batter.upper()} WON!")
    print("#" * 40 + "\n")

if __name__ == "__main__":
    main()