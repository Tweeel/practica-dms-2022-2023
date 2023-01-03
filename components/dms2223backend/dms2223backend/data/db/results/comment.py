"""Comment Class Module
"""

from sqlalchemy import Table, MetaData, Column, String , Integer, ForeignKey # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase

class Comment(ResultBase):
    """ Definition and storage of comment ORM records.
    """

    def __init__(self, discussionid: int,  answerid: int,content: str):
        """ Constructor method.

        Initializes a comment record.

        Args:
            - user (str): A string with the user's name.
            - id (int): A int with the answer's id.

        """

        self.discussionid: int = discussionid
        self.answerid: int = answerid
        self.content: str = content


    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.

        Args:
            - metadata (MetaData): The database schema metadata
                        (used to gather the entities' definitions and mapping)

        Returns:
            - Table: A `Table` object with the table definition.
        """
        return Table(
            'comments',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('discussionid', Integer, nullable=False),
            Column('answerid', Integer, ForeignKey('answers.id'), nullable=False),
            Column('content', String(250), nullable=False)
        )
