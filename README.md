# Mira 3D Format  [![BuildProto](https://github.com/HiceS/mirabuf/actions/workflows/proto_compile.yml/badge.svg)](https://github.com/HiceS/mirabuf/actions/workflows/proto_compile.yml) [![GenerateDocs](https://github.com/HiceS/mirabuf/actions/workflows/docs_gen.yml/badge.svg?branch=main)](https://github.com/HiceS/mirabuf/actions/workflows/docs_gen.yml)

Open source file definition for storing, rendering, and translating physical data from generic 3D model assemblies.

You can find build artifacts from the latest build under the Actions Tab

- python
- cpp
- java

Documentation is available as a Build Artifact for now in the GenerateDocs build action.

[DOCUMENTATION SITE](https://www.mirabuf.dev/) 

## Data Structure

Right now the data structure represents the below diagram, however it is fairly configurable on a per use case basis.

As good general practice it will be instrumental to acknowledge the several ways the data can be stored and have catch cases for them.

### Assembly

Assembly is the first building block that contains the information for the entire model.

- Info
- AssemblyData
- isDynamic
- PhysicalProperites (for entire model)
- GraphContainer (Design) (to represent design hierarchy)
- GraphContainer (Joints) (to represent joint hierarchy)
- Transform (for modeling a additional transform on the entire assembly)

### AssemblyData

This is where all of the actualy Assembly information is stored and referenced from

It contains parent objects for :

- Parts
- Joints
- Materials

These objects can optional be treated as libraries for data if exported alone.

### Parts

For every Part there is a corresponding PartDefinition that contains it's non-unique information.

#### PartDefinition

Contains :

- Bodies / Meshes
- PhysicalProperties
- Transform

#### Part

Uses a Part Definition and can modify the transform to utilize instanced meshes and parts.

- PartDefinition Reference
- Transform
- Joint References

### Materials

Materials are broken into appearance based materials and physical data based materials depending on what is being used.

#### Appearance

Contains information about the display texture for the model.

- Color
- roughness
- specular

#### PhysicalMaterial

Contains information about the following properties for the material

- Thermal Data
- Mechanical Strength Data
- Tensile Strength Data

### Joints

Joints are still a work in progress.

### Types

Universal types used in most of the dedicated files.

#### Info

- Name
- GUID
- Version
- etc..

## Building

### Build All - Single File

#### Windows

`type *.proto > build/mirabuf.proto`

#### OSX

`cat *.proto > build/mirabuf.proto`

#### Build

manually remove syntax statements and imports

` protoc -I=. --python_out=./libs/python --java_out=./libs/java --cpp_out=./libs/cpp ./build/mirabuf.proto `

### Build All - Seperate

` protoc -I=. --python_out=./libs/python --java_out=./libs/java --cpp_out=./libs/cpp ./*.proto `

go, c#, and swift have additional dependencies


#### Python

` protoc -I=. --python_out=./libs/python ./*.proto `

#### Go

` go install google.golang.org/protobuf/cmd/protoc-gen-go `
` protoc -I=. --go_out=./libs/go ./*.proto ` 

#### Java

` protoc -I=. --java_out=./libs/java ./*.proto `

#### CPP

` protoc -I=. --cpp_out=./libs/cpp ./*.proto `

#### C#

` protoc -I=. --csharp_out=./libs/c# ./*.proto `

#### Swift

` protoc -I=. --swift_out=./libs/swift ./*.proto `

#### Rust

`cargo install protobuf-codegen`

`protoc-gen-rust` -- make sure cargo is in path

`protoc --rust_out ./libs/rust *.proto`
