from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def story_start():
	print('story begins...')
	return render_template('index.html')

@app.route('/left')
def dragon_room():
	print('enter the dragon')
	return render_template('left.html')

@app.route('/right')
def ducky_room():
	print('enter the ducky room')
	return render_template('right.html')

@app.route('/fight_dragon')
def fight_dragon():
	print('good luck')
	return render_template('fight_dragon.html')

@app.route('/saved_the_princess')
def saved_the_princess():
	print('you win')
	return render_template('saved_the_princess.html')

@app.route('/you_died')
def you_died():
	print('death becomes you')
	return render_template('you_died.html')

@app.route('/yellow_duck')
def yellow_duck():
	print('ouch')
	return render_template('yellow_duck.html')

@app.route('/cow_duck')
def cow_duck():
	print('nom nom nom')
	return render_template('cow_duck.html')

app.run(debug=True)