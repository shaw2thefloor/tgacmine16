
# This is to deal with inputs to the ContentMine iterative search tool.


class FeatureClassification:
    
    def __init__(self):
        self.categories = {}
    
    def add_class(self, category):
        """
        Add a new item to the list of classes encountered so far.
        Class IDs are normalised in the 0-1 range.
        (I use the name 'category' because 'class' is used for things already by python)
        :return: 
        """
        if len(self.categories) > 0:
            if category not in self.categories:
                self.categories[category] = 1
                # Reorder the numbers from 0 to 1
                i = 0
                for key in self.categories:
                    self.categories[key] = float(i) / float(len(self.categories) - 1)
                    i += 1
        else:
            self.categories[category] = 1
        
    def list_classes(self):
        return sorted(self.categories, key=self.categories.get)

