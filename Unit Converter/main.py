from flet import  *

units = {

	# Length conversion units
	'Length' : {
		'Meter' : 1,
		'Kilometer' : 1000,
		'Centimeter' : 0.01,
		'Milimeter' : 0.001,
		'Micrometer' : 1e-6,
		'Nanometer' : 1e-9,
		'Inch' : 0.0254,
		'Foot' : 0.3048,
		'Yard' : 0.9144,
		'Mile' : 1609.34,
		'Nautical mile' : 1852,
		'Astronomical unit' : 1.496e11,
		'Light year' : 9.461e15,
	},

	#Area conversion units
	'Area': {
		'Square meter': 1,
		'Square kilometer': 1e6,
		'Square centimeter': 1e-4,
		'Square milimeter': 1e-6,
		'Square inch': 0.00064516,
		'Square foot': 0.092903,
		'Hectare': 1e4,
		'Acre' : 4046.86,
	},

	#Volume conversion units
	'Volume' : {
		'Cubic meter' : 1,
		'Cubic centimeter' : 1e-6,
		'Cubic inch' : 1.6387e-5,
		'Cubic foot' : 0.0283168,
		'Liter' : 0.001,
		'Milliliter' : 0.001,
		'US gallon' : 0.001,
		'US quart' : 0.001,
		'US pint' : 0.001,
		'US fluid ounce' : 0.001,
	},

	# Mass conversion units
	'Mass' : {
		'Kilogram' : 1,
		'Gram' : 0.001,
		'Milligram' : 1e-6,
		'Microgram' : 1e-9,
		'Tonne' : 1000,
		'Ounce' : 0.0283495,
		'Pound' : 0.453592,
		'Stone' : 6.35029,
	},

	# Time conversion units
	'Time' : {
		'Second' : 1,
		'Millisecond' : 1e-3,
		'Microsecond' : 1e-6,
		'Nanosecond' : 1e-9,
		'Minutes' : 60,
		'Hours' : 3600,
		'Day' : 86400,
		'Week' : 604800,
		'Year' : 31557600,
	},

	# Speed conversion units
	'Speed' : {
		'Meter per second' : 1,
		'Kilometer per second' : 0.277778,
		'Mile per second' : 0.44704,
		'Centimeter per second' : 0.01,
		'Knot' : 0.514444,
	},

	#Acceleration conversion units
	'Acceleration': {
		'Meter per second squared' : 1,
		'Centimeter per second squared' : 0.0001,
		'Gravity' : 9.80665,
	},

	# Pressure conversion units
	'Pressure' : {
		'Pascal' : 1,
		'Kilopascal' : 1e3,
		'Megapascal' : 1e6,
		'Bar' : 1e5,
		'Millibar' : 1e2,
		'Atmosphere' : 101325,
		'Torr' : 133.322,
		'Psi' : 6894.76,
	},

	'Temperature' : {
		'Celsius': 0,
		'Kelvin' : 0,
		'Fahrenheit' : 0,
	},

	# Energy conversion units
	'Energy' : {
		'Joule' : 1,
		'Kilojoule' : 1e3,
		'Megajoule' : 1e6,
		'Calorie' : 4.184,
		'Kilocalorie' : 4184,
		'Electronvolt' : 1.60218e-19,
		'Watt-hour' : 3600,
		'Kilowatt-hour' : 3.6e6,
	},

	# Power conversion units
	'Power' : {
		'Watt' : 1,
		'Kilowatt' : 1e3,
		'Megawatt' : 1e6,
		'Horsepower' : 735.499,
	},

	# Voltage conversion units
	'Voltage' : {
		'Volt' : 1,
		'Kilovolt' : 1e3,
		'Millivolt' : 1e-3,
	}, 

	# Data size conversion units
	'Data size' : {
		'Bit' : 1,
		'Byte' : 8,
		'Kilobit' : 1000,
		'Kilobyte' : 8000,
		'Megabit' : 1e6,
		'Megabyte' : 8e6,
		'Gigabit' : 1e9,
		'Gigabyte' : 8e9,
		'Terabit' : 1e12,
		'Terabyte' : 8e12,
		'Petabit' : 1e15,
		'Petabyte' : 8e15,
	},
}

def convert_quantity(quantity, value, from_unit, to_unit):
	if quantity == 'Temperature':
		if from_unit == 'Celsius' and to_unit == 'Fahrenheit': return round((value * 9/5) + 32, 3)
		elif from_unit == 'Fahrenheit' and to_unit == 'Celsius' : return round((value - 32) * 5/9, 3)
		elif from_unit == 'Celsius' and to_unit == 'Kelvin': return round(value + 273, 3) 
		elif from_unit == 'Kelvin' and to_unit == 'Celsius': return round(value -273, 3) 
		elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit': return round((value *9/5) - 459.67, 3) 
		elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin': return round((value + 459.67) * 5 / 9, 3)
	else:
		return (value * units [quantity][from_unit]) / units[quantity][to_unit]	


def main(page: Page):
	page.horizontal_alignment = 'center'
	page.window.width = 500
	page.window.height = 610 
	page.window.min_width = 500 
	page.window.min_height = 610 
	page.padding = 20
	page.bgcolor= 'green50'
	page.appbar = AppBar(
		title= Text('Unit_Converter', color='black', size = 25, weight = FontWeight.W_500),
			center_title=True,
			bgcolor='green200'
	)

	def quantity_changed(e):
		main.content.controls[5].content.options = [dropdown.Option(u) for u in units[e.control.value].keys()]
		main.content.controls[6].content.options = [dropdown.Option(u) for u in units[e.control.value].keys()]
		main.content.controls[5].content.value = list(units[e.control.value].keys())[0]
		main.content.controls[6].content.value = list(units[e.control.value].keys())[0]
		main.content.controls[-1].content.value = '---'
		main.content.controls[-2].content.value = ''
		page.update()

	def submit(e):
		main.content.controls[-2].content.focus()
		try:
			output = convert_quantity(
				quantity=main.content.controls[3].content.value,
				value=float(main.content.controls[-2].content.value),
				from_unit=main.content.controls[6].content.value,
				to_unit=main.content.controls[5].content.value,
			)
			main.content.controls[-1].content.value = output
		except:pass
		page.update()

	def swap_units(e):
		main.content.controls[5].content.value,main.content.controls[6].content.value = main.content.controls[6].content.value,main.content.controls[5].content.value
		page.update()
		
	main = Container(
		Stack([
			Card(
				width=420,
				height=95,
				color='green100',
				top=11,
				left=14
			),

			Card(
				width=420,
				height=170,
				color='green100',
				top=109,
				left=14
			),

			Card(
				width=420,
				height=175,
				color='green100',
				top=282,
				left=14
			),

			Container(Dropdown(
				options=[dropdown.Option(u) for u in units.keys()],
				label='Quantity',
				label_style=TextStyle(color='Black'),
				dense=True, scale=1.2, width=180,
				focused_border_color='black',
				value='Length',
				on_change= quantity_changed
			), top=34, left=53),

			FloatingActionButton(
				content=Text(
					'Convert',
					size=20,
					color='black'
				),
				top=28.8, left = 265,
				bgcolor='green300',
				width=150, height=58.5,
				shape= RoundedRectangleBorder(radius = 6),
				on_click=submit
			),

			Container(Dropdown(
				options=[dropdown.Option(u) for u in units['Length'].keys()],
				label='Output Unit',
				label_style=TextStyle(color='Black'),
				dense=True, scale=1.2, width=280,
				focused_border_color='black',
				value='Meter'
			), top=206, left=63),

			Container(Dropdown(
				options=[dropdown.Option(u) for u in units['Length'].keys()],
				label='Input Unit',
				label_style=TextStyle(color='Black'),
				dense=True, scale=1.2, width=280,
				focused_border_color='black',
				value='Meter'
			), top=136, left=63),

			IconButton(
				icon=icons.SWAP_CALLS,
				icon_size=35,
				icon_color='black',
				top=166, left=373,
				on_click=swap_units
			),

			Container(TextField(
				label='Input Value',
				label_style=TextStyle(color='Black'),
				width=310,
				scale=1.2,
				dense=True,
				focused_border_color='black',
				cursor_color='black',
				text_align='center',
				on_submit=submit
			), top=309, left=68),

			Container(TextField(
				label='Output Value',
				value='---',
				label_style=TextStyle(color='Black'),
				width=310,
				scale=1.2,
				dense=True,
				focused_border_color='black',
				cursor_color='black',
				text_align='center',
				read_only=True,
				on_submit=submit
			), top=382, left=68),
		]),
		width = 450 ,height = 472,
		bgcolor='green50',
		border_radius = 15,
		shadow = BoxShadow(spread_radius=2, blur_radius=9, color='bluegrey200')
	)

	page.add(main)
	
app(main)