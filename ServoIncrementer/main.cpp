#include <iostream>

using namespace std;

void angle_write(int angle);

int main() {
	// Create and initialize variables
	int desired_angle, current_angle, increment_angle, delta_angle, remainder_angle;
	increment_angle = 5;

	// Get the angles from the user
	cout << "Enter the current angle: "; cin >> current_angle;
	cout << "Enter the desired angle: "; cin >> desired_angle;

	// Calculate the desired angle and remainder
	delta_angle = desired_angle - current_angle;   	 // Calculate the difference between the desired angle and the current angle
	remainder_angle = delta_angle % increment_angle; // Calculate the remainder of the delta angle divided by the increment step size

	// Move the remainder
	if (remainder_angle) {
		current_angle += delta_angle % increment_angle;
		angle_write(current_angle);
	}

	// Move the rest
	while (current_angle != desired_angle) {
		if (current_angle > desired_angle) { current_angle -= increment_angle; }
		else { current_angle += increment_angle; }
		angle_write(current_angle);
	}

	// Exit without errors
	return 0;
}

void angle_write(int angle) {
	cout << angle << endl;
}
