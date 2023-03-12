#Schemas convert our file to json file
from apiflask.schemas import Schema
from apiflask import fields



"""
  class Task:
    id int
    content string
    date_added datetime
    is_completed Boolean
  """





class TaskOutputSchema(Schema):
  id = fields.Integer()
  content = fields.String()
  date_added = fields.DateTime()
  is_completed = fields.Boolean()

class TaskCreateSchema(Schema):  #or InputSchema
  content = fields.String(required=True)


class TaskUpdateSchema(Schema):
  content = fields.String(required=True)
  is_completed = fields.Boolean(required=True)

class DeleteAllTasksSchema(Schema):
    pass


