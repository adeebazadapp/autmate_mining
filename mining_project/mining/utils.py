import random
from .models import MiningData

def run_mining_script():
    # Example: Simulating data mining
    name = f"DataPoint-{random.randint(1, 100)}"
    value = random.uniform(10.0, 100.0)

    # Save data to SQL database
    mined_data = MiningData(name=name, value=value)
    mined_data.save()
    return mined_data
