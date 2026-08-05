class Analytics:

    def analyze(self, result):

        cars = 0
        people = 0

        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = result.names[class_id]

            print(class_id, class_name)

            if class_name == "car":
                cars += 1

            elif class_name == "person":
                people += 1


        if cars > 12:
            traffic = "Heavy"
            alert = True

        elif cars > 6:
            traffic = "Moderate"
            alert = False

        else:
            traffic = "Low"
            alert = False


        return {
            "cars": cars,
            "people": people,
            "traffic": traffic,
            "alert": alert
        }