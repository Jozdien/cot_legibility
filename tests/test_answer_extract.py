from datasets import load_from_disk

def get_actual_answer(question_text, dataset):
    """Find the matching answer in the dataset."""
    # Find the matching question in the dataset
    for item in dataset:
        if item['Question'].strip() == question_text.strip():
            return item['Correct Answer']
    return "No matching answer found"

QUESTION = "Researchers are attempting to detect transits of two Earth-like planets: Planet_1 and Planet_2. They have limited observing time and want to observe the one that has the highest probability of transiting. Both of these planets have already been detected via the RV method, allowing us to know their minimum masses and orbital periods. Although both planets share the same masses, the orbital period of Planet_1 is three times shorter than that of Planet_2. Interestingly, they both have circular orbits. Furthermore, we know the masses and radii of the host stars of these two planets. The star hosting Planet_1 has a mass that is twice that of the host star of Planet_2. As the host of Planet_2 is slightly evolved, both host stars have the same radii. Based on the provided information, the researchers have chosen to observe:"

# Load the GPQA dataset
dataset_path = "../data/gpqa_diamond"
gpqa_dataset = load_from_disk(dataset_path)

actual_answer = get_actual_answer(QUESTION, gpqa_dataset)
print(actual_answer)