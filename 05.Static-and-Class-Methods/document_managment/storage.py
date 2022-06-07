class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = '\n'.join([repr(d) for d in self.documents])
        return result

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        edited_category = [e for e in self.categories if e.id == category_id][0]
        self.categories.remove(edited_category)
        edited_category.name = new_name
        self.categories.append(edited_category)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        edited_topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(edited_topic)
        edited_topic.topic = new_topic
        edited_topic.storage_folder = new_storage_folder
        self.topics.append(edited_topic)

    def edit_document(self, document_id, new_file_name):
        edited_document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(edited_document)
        edited_document.file_name = new_file_name
        self.documents.append(edited_document)

    def delete_category(self, category_id):
        edited_category = [e for e in self.categories if e.id == category_id][0]
        self.categories.remove(edited_category)

    def delete_topic(self, topic_id):
        edited_topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(edited_topic)

    def delete_document(self, document_id):
        edited_document = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(edited_document)

    def get_document(self, document_id):
        doc = [d for d in self.documents if d.id == document_id][0]
        return doc