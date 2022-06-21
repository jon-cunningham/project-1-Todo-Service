from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import uuid


def generate_id():
    # return an uuid as a string for id
    return str(uuid.uuid4())


class TodoModel(Model):
    """
    TODO TABLE
    """
    class Meta:
        table_name = 'todo'
    pk = UnicodeAttribute(hash_key=True, default="TODO")
    id = UnicodeAttribute(range_key=True, default=generate_id())
    title = UnicodeAttribute(null=False)
    notes = UnicodeAttribute(default="Add a note?")
    status = UnicodeAttribute(default="Task in progress")


# if table does not exist create it
if not TodoModel.exists():
    TodoModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
