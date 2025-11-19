"""Add profile picture support to videos table

Revision ID: add_profile_picture_support
Revises: 7fcaba3ee0c1
Create Date: 2025-11-17 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add_profile_picture_support'
down_revision: Union[str, None] = '7fcaba3ee0c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Agregar columna usuario_id a tabla videos (nullable para mantener compatibilidad)
    op.add_column('videos', sa.Column('usuario_id', sa.Integer(), nullable=True))
    
    # Agregar columna tipo a tabla videos con valor por defecto 'video'
    op.add_column('videos', sa.Column('tipo', sa.String(50), server_default='video', nullable=True))
    
    # Hacer nullable la columna producto_id
    op.alter_column('videos', 'producto_id', existing_type=sa.Integer(), nullable=True)
    
    # Agregar foreign key para usuario_id
    op.create_foreign_key(
        'fk_videos_usuario_id',
        'videos', 'usuarios',
        ['usuario_id'], ['id_usuario'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Eliminar foreign key
    op.drop_constraint('fk_videos_usuario_id', 'videos', type_='foreignkey')
    
    # Eliminar columnas
    op.drop_column('videos', 'tipo')
    op.drop_column('videos', 'usuario_id')
    
    # Revertir nullable en producto_id
    op.alter_column('videos', 'producto_id', existing_type=sa.Integer(), nullable=False)
