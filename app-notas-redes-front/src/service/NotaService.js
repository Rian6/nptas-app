import {post, get, put, del} from '../conection/fetchConection'
  
const salvar = (nota) =>{
  return post("salvar", nota)
}

const editar = (nota) =>{
    return put("editar", nota)
  }

const findAll = () => {
    return get("findAll")
}

const deleteById = (id) => {
    return del("deletar/"+id)
}

export {
    salvar,
    findAll,
    editar,
    deleteById
}