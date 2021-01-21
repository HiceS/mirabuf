# Mira 3D Format
Open source file definition for storing rendering and physical data from 3D model assemblies.

## Data Structure

Right now the data structure represents the below diagram, however it is fairly configurable on a per use case basis.
As good general practice it will be instrumental to acknowledge the several ways the data can be stored and have catch cases for them.

#### Info:
- Name
- GUID
- Version
- etc..

#### Assembly:
- Info (Physical, Author, etc)
- Part Data (All of the assembly model data)
- Design Hierarchy (Hierarchy of Design Occurreces and Transforms)
- joint Hierarchy (detached graph to represent compound bodies)

#### Part Data:
- Joints Map (DAG of joint data with accepted orphaned nodes)
- PartDefinition Map (Mapping of all unique design elements)
- Part Map (Mapping of each Part with reference to PartDefinition)
- Rendering Material Map
- Physical Material Map

#### PartDefinition:
- Info
- [Optional] Body List
- Physical Attributes

#### Part:
(all of these are modifiers to PartDefinition)
- Info
- PartDefRef
- Transform
    - Translation elements (rot - pos)
- [Optional] list of design children
- [Optional] Joint List

#### Body:
(always unique)
- Info
- PartRef (for bi-directional traversal where needed)
- Triangle Mesh


#### Triangle Mesh:
- Indicies
- Verts
- Norms
- UV Map

## Building

#### Python

` protoc -I=. --python_out=./libs/python ./*.proto ` -> builds to the lib/python folder

