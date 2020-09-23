import src.acquire
import src.prepare
import src.explore
import src.model

# python main.py
if __name__ == "__main__":
    src.acquire.run()
    src.scrub.run()
    src.explore.run()
    src.model.run()